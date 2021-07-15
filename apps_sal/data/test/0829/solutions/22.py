k = int(input())
s = input()
num = s.count("1")
if num == k // 2 and k % 2 == 0:
    print(2)
    print(s[:k-1],s[-1])
else:
    print(1)
    print(s)

