size = int(input()) - 1
string = input()
keys = [string[2 * i] for i in range(size)]
rooms = [string[2 * i + 1] for i in range(size)]

must_buy = 0
key_count = [0 for i in range(26)]
for i in range(size):
    key_count[ord(keys[i]) - ord('a')] += 1
    key_count[ord(rooms[i]) - ord('A')] -= 1
    if key_count[ord(rooms[i]) - ord('A')] < 0:
        key_count[ord(rooms[i]) - ord('A')] += 1
        must_buy += 1

print(must_buy)
