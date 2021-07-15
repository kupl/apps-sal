def f(a, b):
    return a <= b and not 2 * a >= b

V1, V2, V3, Vm = map(int, input().split())
for v1 in range(V1, 2 * V1 + 1):
    for v2 in range(V2, min(2 * V2 + 1, v1)):
        for v3 in range(V3, min(2 * V3 + 1, v2)):
            if f(Vm, v1) and f(Vm, v2) and Vm <= v3 <= 2 * Vm:
                print(v1, v2, v3, sep='\n')
                return
print(-1)

