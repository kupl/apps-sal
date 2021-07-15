s = input()
k = int(input())

length = len(s)
tokenLength = length / k

if length % k != 0:
    print("NO")
    return

for i in range(k):
    toCheck = s[i * int(tokenLength) : i * int(tokenLength) + int(tokenLength)]
    if toCheck != toCheck[::-1]:
        print("NO")
        return

print("YES")

