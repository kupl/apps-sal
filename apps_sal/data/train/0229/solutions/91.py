class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if len(A) == 0 :
            return True
        
        mydict = {}
        for _ in range(0,len(A)):
            if A[_] in mydict:
                mydict[A[_]] += 1
            else:
                mydict[A[_]] = 1
        
        A_sorted = sorted(A)
        
        #print(A_sorted)
        #print(mydict)
        not_valid = set()
        for num in A_sorted:
            if len(mydict) == 0:
                return True 
            if num in not_valid:
                continue
                
            if (2 * num) in mydict and num in mydict:
                double = 2*num
                mydict[num] -= 1
                mydict[double] -= 1

                if mydict[num] == 0:
                    mydict.pop(num)
                    not_valid.add(num)
                #deals with duplicates
                if num == double:
                    continue
                elif mydict[2*num] == 0:
                    mydict.pop(2*num)
                    not_valid.add(2*num)
            elif (num/2 in mydict and num in mydict):
                half = num/2
                mydict[num] -= 1
                mydict[num/2] -= 1

                if mydict[num] == 0:
                    mydict.pop(num)
                    not_valid.add(num)
                if mydict[num/2] == 0:
                    mydict.pop(num/2)
                    not_valid.add(num/2)
            else:
                return False
