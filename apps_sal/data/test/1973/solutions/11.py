n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    d[a[i]] = 0


# numOdd = 0
# for i in range(n):
# 	d[a[i]] += 1

# 	if(d[a[i]] % 2 != 0):
# 		numOdd += 1

# 	else:
# 		numOdd -= 1

# 	if(numOdd == 1):
# 		x = i+1

# print(x)

x = 1
for i in range(1, n):
    if(a[i] == a[i - 1]):
        # print("yo")
        x = i + 1
    else:
        break

for i in range(n):
    d[a[i]] += 1

    l = list(d.values())
    l = list(set(l))
    ll = list(d.values())
    l.sort()
    # print(l)
    if(l[0] == 0):
        l.pop(l[0])

    if(len(l) == 2):
        if(abs(l[0] - l[1]) == 1 and ll.count(l[1]) == 1):
            x = max(x, i + 1)
        elif(l[0] == 1 and ll.count(1) == 1):
            x = max(x, i + 1)
    if(len(l) == 1 and l[0] == 1):
        x = max(x, i + 1)

print(x)
