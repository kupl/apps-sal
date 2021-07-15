like_count = int(input())
likes = input().split()
counter = {}
most_liked = ''
max_like_count = 0
for like in likes:
    if like in counter:
        counter[like] += 1
    else:
        counter[like] = 1
    if max_like_count < counter[like]:
        most_liked = like 
        max_like_count = counter[like]
print(int(most_liked))
