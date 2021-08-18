N = int(input())
slist = [x == "o" for x in input()]

answer_list = [0] * N

ok = False
for p1, p2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    answer_list[0] = p1
    answer_list[1] = p2

    for i in range(2, N):
        if answer_list[i - 1] == 1:
            if slist[i - 1]:
                answer_list[i] = answer_list[i - 2]
            else:
                answer_list[i] = -answer_list[i - 2]
        else:
            if slist[i - 1]:
                answer_list[i] = -answer_list[i - 2]
            else:
                answer_list[i] = answer_list[i - 2]

    contra = False
    for i in range(N):
        l = (i - 1) % N
        r = (i + 1) % N
        if answer_list[i] == 1:
            if slist[i]:
                if answer_list[l] != answer_list[r]:
                    contra = True
            else:
                if answer_list[l] == answer_list[r]:
                    contra = True
        else:
            if slist[i]:
                if answer_list[l] == answer_list[r]:
                    contra = True
            else:
                if answer_list[l] != answer_list[r]:
                    contra = True

    if not contra:
        ok = True
        break

if ok:
    sw_list = []
    for ans in answer_list:
        if ans == 1:
            sw_list.append("S")
        else:
            sw_list.append("W")
    print("".join(sw_list))
else:
    print(-1)
