n = int(input())
p = list(map(int, input().split()))

ans = []
left = 1
MIN = 1
while left < n:
    # 小さい数から順に確定していく
    # 移動前の位置より左はもう動かせない
    for i in range(left, n):
        if p[i] == MIN:
            # 確定した数が正しい位置にいるか
            for j in range(left-1, i-1):
                MIN = max(MIN, p[j])
                if p[j] != j+2:
                    print(-1)
                    return
            ans.extend(range(i,left-1,-1))
            p[i] = p[i-1]
            break
    else:
        print(-1)
        return
    left = i+1
    MIN += 1
print(*ans, sep='\n')
