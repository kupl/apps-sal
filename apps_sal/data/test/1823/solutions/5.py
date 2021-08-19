(num_days, num_genres) = list(map(int, input().split()))
schedule = list(map(int, input().split()))
compressed = []
current = schedule[0]
pos = 1
while True:
    compressed.append(current)
    while pos < num_days and schedule[pos] == current:
        pos += 1
    if pos < num_days:
        current = schedule[pos]
    else:
        break
score = (num_genres + 1) * [0]
score[compressed[0]] += 1
for i in range(2, len(compressed)):
    score[compressed[i - 1]] += 1
    if compressed[i - 2] == compressed[i]:
        score[compressed[i - 1]] += 1
score[compressed[len(compressed) - 1]] += 1
(best_score, best_genre) = (-1, -1)
for genre in range(1, num_genres + 1):
    if score[genre] > best_score:
        best_score = score[genre]
        best_genre = genre
print(best_genre)
