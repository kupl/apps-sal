n = int(input())
string = input()

i = 1
cnt = 0
while cnt < n:
    print(string[cnt], end="")

    cnt += i
    i += 1

