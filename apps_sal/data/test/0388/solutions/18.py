names = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] + ['AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'[i:i + 2] for i in range(0, len('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'), 2)]
(n, k) = map(int, input().split())
yes_no = input().split()
guess = names[:n]
for i in range(len(yes_no)):
    if yes_no[i] == 'NO':
        guess[i + k - 1] = guess[i]
print(' '.join(guess))
