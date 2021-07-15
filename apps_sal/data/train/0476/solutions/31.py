class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for each car:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i], (target - position[i]) / speed[i]])
        
        cars.sort(key=lambda x: x[0])
        #print(cars)
        
        maxs = []
        for car in cars[::-1]:
            if not maxs: maxs.insert(0, car[2])
            else: maxs.insert(0, max(maxs[0], car[2]))
        print(maxs)
        fleets = {}
        fleetCount = 0
        
        for i, car in enumerate(cars):
            inFleet = maxs[i+1] >= car[2] if i < len(cars)-1 else False
            if not inFleet:
                fleetCount+=1
        
        return fleetCount
