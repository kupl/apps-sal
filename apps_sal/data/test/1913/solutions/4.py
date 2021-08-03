n = int(input())
A = list(input().split())
answerzero = 0
answer = "1"
for elem in A:
    if elem == "0":
        print(0)
        break
    if elem.count("1") == 1 and elem.count("0") == len(elem) - 1:
        answerzero += len(elem) - 1
    else:
        answer = elem
else:
    print(answer + "0" * answerzero)
