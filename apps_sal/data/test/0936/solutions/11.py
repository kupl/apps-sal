photos = {}
n = input()
likes = input().split()
m = {'id': 0, 'q': 0}
for p_id in likes:
    if p_id in photos:
        photos[p_id] += 1
    else:
        photos[p_id] = 1
    if photos[p_id] > m['q']:
        m['q'] = photos[p_id]
        m['id'] = p_id
print(m['id'])
