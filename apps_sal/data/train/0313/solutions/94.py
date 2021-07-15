# check length of array with total number of flowers needed- 
#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/691031/Python3-Binary-Search-(ELIF5%3A-Explained-Like-I'm-5-Years-Old)
class Solution:
    def minDays(self, listOfFlowerBloomDays: List[int], targetNumberOfBouquets: int, flowersPerBouquet: int) -> int:
        def numberOfBouquetsWeCanMakeOnThisDay(dayThatWeAreChecking):
            
            currentListOfAdjacentBloomedFlowers = []
            numberOfBouquetsWeCanMakeOnThisDay = 0
            
            for dayThatFlowerBlooms in listOfFlowerBloomDays: 
                if dayThatFlowerBlooms <= dayThatWeAreChecking:
                    currentListOfAdjacentBloomedFlowers.append('x')   
                else:
                    numberOfBouquetsWeCanMakeOnThisDay += len(currentListOfAdjacentBloomedFlowers)//flowersPerBouquet
                    currentListOfAdjacentBloomedFlowers = []

            numberOfBouquetsWeCanMakeOnThisDay += len(currentListOfAdjacentBloomedFlowers)//flowersPerBouquet
                    
            return numberOfBouquetsWeCanMakeOnThisDay
        
        totalNumberOfFlowersNeeded = targetNumberOfBouquets*flowersPerBouquet
        numberOfFlowersWeCanGrow = len(listOfFlowerBloomDays)
        
        if numberOfFlowersWeCanGrow < totalNumberOfFlowersNeeded: 
            return -1
        
        leftDay = 0
        rightDay = max(listOfFlowerBloomDays)
        
        while leftDay < rightDay:
            
            currentDay = leftDay + (rightDay-leftDay)//2
            if numberOfBouquetsWeCanMakeOnThisDay(currentDay) < targetNumberOfBouquets:
                leftDay = currentDay+1
            else:
                rightDay = currentDay

        return leftDay
