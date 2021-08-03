n = int(input())
l = input().split(" ")
first = 0
while first <= n - 1 and l[first] == "0":
    first += 1
if first == n:
    print(0)
else:
    last = n - 1
    while last >= 0 and l[last] == "0":
        last -= 1
    count = 0
    divide = []
    for i in range(first, last + 1):
        if(l[i] == "0"):
            count += 1
        else:
            divide.append(count + 1)
            count = 0
    ans = 1
    for i in range(len(divide)):
        ans *= divide[i]
    print(ans)
