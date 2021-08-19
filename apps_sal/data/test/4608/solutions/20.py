import sys
nyuryoku = [int(i) - 1 for i in sys.stdin]
N = nyuryoku[0] + 1
a_list = nyuryoku[1:]
cnt_push = 0
button_list = [False] * N
i = 0
while True:
    if button_list[i] == False:
        button_list[i] = True
        cnt_push += 1
        if a_list[i] == 1:
            break
        i = a_list[i]
    else:
        cnt_push = -1
        break
print(cnt_push)
'\nimport sys\n\nl = [int(i) - 1 for i in sys.stdin]\n\nN = l[0] + 1\n\na = l[1:]\n\ndone = [False] * N\n\ni = 0\n\nans = 0\n\nwhile True:\n    if done[i] == False:\n        done[i] = True\n        ans += 1\n        if a[i] == 1:\n            break\n        i = a[i]\n    else:\n        ans = -1\n        break\n\nprint(ans)\n'
