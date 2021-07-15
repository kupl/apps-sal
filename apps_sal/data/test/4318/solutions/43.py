N = int(input())
H = map(int,input().split())
height_list = list(H)
# print(height_list)
Inn = []
Ocean_view = []

# Ocean_view.append(height_list[0])
i=0
for j in range(N):
    Inn.append(height_list[i])
    if height_list[i] == max(Inn):
        Ocean_view.append(height_list[i])

    i += 1

print(len(Ocean_view))
