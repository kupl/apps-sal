t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    num = s.find(">")
    num2 = s.rfind("<")
    if num == -1 or num2 == -1:
        print(0)
    else:
        print(min(num,n - 1 - num2))

