N = int(input())
As = list(map(int, input().split()))

abs_As = []
negative_count = 0

for A in As:
    if(A <= 0):
        abs_As.append(abs(A))
        negative_count += 1

    else:
        abs_As.append(A)


if(negative_count % 2 == 0):
    print(sum(abs_As))

else:
    print(sum(abs_As) - 2 * min(abs_As))
