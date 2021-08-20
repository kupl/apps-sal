from collections import Counter
num_moves = int(input())
move_count = Counter(input())
print(num_moves - abs(move_count['R'] - move_count['L']) - abs(move_count['U'] - move_count['D']))
