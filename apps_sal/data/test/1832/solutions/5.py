for _ in range(int(input())):
    _ = int(input())
    *arr, = list(map(int, input().split()))
    max_len = max(arr) + 1
    ans = ['a'] * max_len
    print(''.join(ans))
    for n in arr:
        if ans[n] == 'a':
            ans[n] = 'b'
        else:
            ans[n] = 'a'
        print(''.join(ans))
