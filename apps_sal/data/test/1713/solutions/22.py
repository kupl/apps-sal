string = input()
numbers = list(map(int, string.split()))
s, t = numbers[1], numbers[2]
string = input()
glasses = list(map(int, string.split()))
temp = s
a = 0
while temp != t:
    temp = glasses[temp - 1]
    if temp == s:
        print(-1)
        break
    a += 1
else:
    print(a)
