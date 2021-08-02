n = int(input())
wn = list(map(int, input().split()))
if sum(wn) % 200 == 0 and n % 2 != 1:
    print("YES")
elif sum(wn) // n == 200:
    print("NO")
elif sum(wn) % 200 != 0:
    print("NO")
else:
    print("YES")
