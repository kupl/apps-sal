n = int(input())
a = list(map(int, input().split()))
odd = 0
even = 0
for i in a:
    if i % 2 != 0:
        odd += 1
    else:
        even += 1
if odd <= even:
    print(min(odd, even))
else:
    diff = odd - even
    print(min(odd, even) + diff // 3)
