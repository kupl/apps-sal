n = int(input())
positions = input().split()
s1 = set()
l1 = [1] * (n - 1)
s2 = set()
l2 = []
count = 0
for i in range(n - 1):
    if positions[i] in s1:
        l1[i] = 0
    s1.add(positions[i])
for i in range(n - 1):
    s2.add(positions[-1 - i])
    l2.append(len(s2))
for i in range(n - 1):
    count += l1[i] * l2[-1 - i]
print(count)
