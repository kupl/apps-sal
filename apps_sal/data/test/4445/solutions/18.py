n = int(input())
arr = list(map(int, input().split()))
even, odd = [], []

for i in arr:
    if i % 2 == 0:
        even += [i]
    else:
        odd += [i]

even = sorted(even)
odd = sorted(odd)

if len(even) == len(odd):
    print(0)
    return

elif len(even) < len(odd):
    even, odd = odd, even

#print(even, odd)

even.pop()
while even and odd:
    even.pop()
    odd.pop()

#print(even, odd)
print(sum(even))
