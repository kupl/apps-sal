S = input()
DAY = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for num in range(7):
    if DAY[num] == S:
        print((7 - num))
