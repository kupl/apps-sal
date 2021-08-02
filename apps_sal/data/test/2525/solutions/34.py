def main():
    S = input()
    Q = int(input())
    order = [list(input().split()) for _ in range(Q)]
    left_flag = 0
    right_flag = 0
    cnt = 0
    for i in range(Q):
        if order[i][0] == '1':
            cnt += 1
        else:
            if cnt % 2 == 0:
                if order[i][1] == '1':
                    if left_flag == 1:
                        left = order[i][2] + left
                    else:
                        left = order[i][2]
                        left_flag = 1
                else:
                    if right_flag == 1:
                        right = right + order[i][2]
                    else:
                        right = order[i][2]
                        right_flag = 1
            else:
                if order[i][1] == '2':
                    if left_flag == 1:
                        left = order[i][2] + left
                    else:
                        left = order[i][2]
                        left_flag = 1
                else:
                    if right_flag == 1:
                        right = right + order[i][2]
                    else:
                        right = order[i][2]
                        right_flag = 1
    if left_flag == 1 and right_flag == 1:
        S = left + S + right
    elif left_flag == 1 and right_flag == 0:
        S = left + S
    elif left_flag == 0 and right_flag == 1:
        S = S + right
    else:
        S = S

    if cnt % 2 == 0:
        return(S)
    else:
        S2 = S[-1]
        for i in range(len(S) - 2, -1, -1):
            S2 = S2 + S[i]
        return S2


print((main()))
