N = int(input())
A = list(map(int, input().split()))
d = {"A": 0, "D": 0}
for number in A:
    if number % 2 == 0:
        if number % 3 == 0 or number % 5 == 0:
            d["A"] += 1
        else:
            d["D"] += 1
    else:
        d["A"] += 1

if d["D"] > 0:
    print("DENIED")
else:
    print("APPROVED")
