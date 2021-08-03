n1, n2 = list(map(int, input().split()))
polish_words = []
enemy_words = []
common_words = []
for i in range(n1):
    polish_words.append(input())
for i in range(n2):
    s = input()
    enemy_words.append(s)
    if s in polish_words:
        common_words.append(s)
polish_count = len(polish_words) - len(common_words)
enemy_count = len(enemy_words) - len(common_words)
if len(common_words) % 2 == 1:
    polish_count += 1
if polish_count >= enemy_count + 1:
    print('YES')
else:
    print('NO')
