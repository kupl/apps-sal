N = int(input())
M = {'R': [], 'L': [], 'U': [], 'D': [], 'X': [], 'Y': []}
for _ in range(N):
    x, y, d = input().split()
    if d in ['R', 'L']:
        M[d].append(int(x))
        M['Y'].append(int(y))
    else:
        M['X'].append(int(x))
        M[d].append(int(y))
for d in 'RLDUXY':
    M[d] = sorted(M[d])
T = [0] * 13
T[0] = M['X'][0] - M['R'][0] if M['X'] and M['R'] else -1
T[1] = M['L'][0] - M['X'][0] if M['X'] and M['L'] else -1
T[2] = (M['L'][0] - M['R'][0]) / 2 if M['L'] and M['R'] else -1
T[3] = M['X'][-1] - M['R'][-1] if M['X'] and M['R'] else -1
T[4] = M['L'][-1] - M['X'][-1] if M['X'] and M['L'] else -1
T[5] = (M['L'][-1] - M['R'][-1]) / 2 if M['L'] and M['R'] else -1
T[6] = M['Y'][-1] - M['U'][-1] if M['Y'] and M['U'] else -1
T[7] = M['D'][-1] - M['Y'][-1] if M['Y'] and M['D'] else -1
T[8] = (M['D'][-1] - M['U'][-1]) / 2 if M['D'] and M['U'] else -1
T[9] = M['Y'][0] - M['U'][0] if M['Y'] and M['U'] else -1
T[10] = M['D'][0] - M['Y'][0] if M['Y'] and M['D'] else -1
T[11] = (M['D'][0] - M['U'][0]) / 2 if M['D'] and M['U'] else -1
Rect = [-1] * 13
for i, t in enumerate(T):
    if t < 0:
        continue
    R = []
    L = []
    U = []
    D = []
    if M['R']:
        R.append(M['R'][-1] + t)
        L.append(M['R'][0] + t)
    if M['L']:
        R.append(M['L'][-1] - t)
        L.append(M['L'][0] - t)
    if M['U']:
        U.append(M['U'][-1] + t)
        D.append(M['U'][0] + t)
    if M['D']:
        U.append(M['D'][-1] - t)
        D.append(M['D'][0] - t)
    if M['X']:
        R.append(M['X'][-1])
        L.append(M['X'][0])
    if M['Y']:
        U.append(M['Y'][-1])
        D.append(M['Y'][0])
    Rect[i] = (max(R) - min(L)) * (max(U) - min(D))
print(min([r for r in Rect if r >= 0]))
