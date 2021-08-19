N = int(input())
L = map(int, input().split())

# L = sorted(L)

# Total = 0
# for i in range(N*2):
# 	if(i%2==0):
# 		Total+=L[i]

# print(Total)


def skewer(input):
    x = sorted(input, reverse=True)
    result = 0
    for i in range(0, len(x)):
        if i % 2 == 1:
            result = result + x[i]
    return result


print(skewer(L))
