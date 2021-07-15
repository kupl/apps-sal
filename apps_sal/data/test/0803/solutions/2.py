n = int(input())
s = input()
standing = s.count("X")
count = abs(n // 2 - standing)
print(count)
if standing < n // 2:

    print(str.replace(s, "x", "X", count))

else:

    print(str.replace(s, "X", "x", count))

