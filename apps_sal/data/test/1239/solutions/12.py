def main():
    n = int(input())
    cities = list(map(int, input().split()))

    cities.sort()
    
    minimum = float('inf')
    count = 0

    for i in range(len(cities)-1):
        dif = abs(cities[i]-cities[i+1])
        if dif == minimum:
            count += 1
        elif dif < minimum:
            minimum = dif
            count = 1

    print(minimum, count)
        

def __starting_point():
    main()

__starting_point()
