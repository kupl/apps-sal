def input2():
    return map(int, input().split())


def input_array():
    return list(map(int, input().split()))


n, q = input2()
B = str(input())
LR = [input_array() for _ in range(q)]

T = [0] * (n + 1)

for i in range(n):
    if B[i:i + 2] == "AC":
        T[i + 1] = T[i] + 1
    else:
        T[i + 1] = T[i]
for lr in LR:
    st = lr[0] - 1
    fi = lr[1] - 1
    print(T[fi] - T[st])
