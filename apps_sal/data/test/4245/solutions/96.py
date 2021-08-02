A, B = map(int, input().split())
answer = 1
plug = A

if B == 1:
    print(0)
    return

while B > A:
    answer += 1
    A += (plug - 1)


print(answer)
