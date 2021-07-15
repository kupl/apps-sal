seat_secs = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}

vasya = input()
row = int(vasya[:-1]) - 1
seat = vasya[-1]
seconds = 0
if row % 4 == 0 or row % 4 == 2: seconds += (row//4) * 16
else: seconds += (row//4) * 16 + 7
seconds += seat_secs[seat]
print(seconds)


