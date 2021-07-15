x = 0
res = 0
n, m, mn, mx = list(map(int, input().split()))
lst = list(map(int, input().split()))
for i in range(m):
    if lst[i] < mn or lst[i] > mx:
        res = "Incorrect"
        break
    if lst[i] == mn:
        x = 1
    elif lst[i] == mx:
        x = 1
if res == "Incorrect":
    print(res)
else:
    if n - m >= 2 - x:
        print("Correct")
    else:
        print("Incorrect")

