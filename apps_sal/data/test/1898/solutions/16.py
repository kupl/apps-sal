n = int(input())
print('I hate', end = ' ')
for i in range(n - 1):
    word = 'hate'
    if i % 2 == 0:
        word = 'love'
    print('that I ' + word, end = ' ')
print('it')
