from collections import deque
K = int(input())
S = [i for i in range(1, 10)]
S = deque(S)
for i in range(1, K + 1):
    Lun = S.popleft()
    Lu = Lun % 10
    if Lu != 0:
        S.append(10 * Lun + Lu - 1)
    S.append(Lun * 10 + Lu)
    if Lu != 9:
        S.append(10 * Lun + Lu + 1)
print(Lun)
