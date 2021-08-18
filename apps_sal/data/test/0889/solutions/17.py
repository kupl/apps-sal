__author__ = "runekri3"

BOX_INDEXES = [
    [0, 1, 4, 5],
    [1, 2, 5, 6],
    [2, 3, 6, 7],
    [4, 5, 8, 9],
    [5, 6, 9, 10],
    [6, 7, 10, 11],
    [8, 9, 12, 13],
    [9, 10, 13, 14],
    [10, 11, 14, 15]]

data = ""
for _ in range(4):
    data += input("")

result = "NO"
for box_index in BOX_INDEXES:
    hashtag_count = 0
    for index in box_index:
        if data[index] == "
        hashtag_count += 1
    if hashtag_count != 2:
        result = "YES"
        break
print(result)
