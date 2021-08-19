(n, m, k) = list(map(int, input().split()))
H = set(map(int, input().split()))
bone_pos = 1
if bone_pos not in H:
    for i in range(k):
        (u, v) = list(map(int, input().split()))
        if bone_pos == u:
            bone_pos = v
        elif bone_pos == v:
            bone_pos = u
        if bone_pos in H:
            break
print(bone_pos)
