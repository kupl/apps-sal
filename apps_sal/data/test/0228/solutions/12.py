n = int(input())
a = [int(x) for x in input().split()]
mn, cnt = min(a), 0
for i in a:
    if i == mn:
        cnt += 1
print("Alice" if cnt <= int(n / 2) else "Bob")
