s = int(input())

for i in range(1,11):
    if s <= i * 1000:
        ans = i * 1000 - s
        print(ans)
        break
