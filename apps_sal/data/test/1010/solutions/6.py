n = int(input())
isnut = [(int(x) == 1) for x in input().split()]
ans = 1
stack = 1
hasnut = False
for nut in isnut:
    if nut:
        if hasnut:
            ans *= stack
            stack = 1
        else:
            hasnut = True
            stack = 1
    else:
        stack += 1
print(ans if hasnut else 0)

