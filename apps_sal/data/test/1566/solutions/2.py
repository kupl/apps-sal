def main():
    size = int(input())
    sq = [[int(c) for c in input().strip()] for _ in range(size)]
    print('Yes' if haslair(sq) else 'No')
        
def haslair(sq):
    corners = [(r, c) for r, row in enumerate(sq) for c, count in enumerate(row)
                if count==1]
    if len(corners) != 4:
        return False
    left, right, top, bottom = corners[0][1], corners[3][1], corners[0][0], corners[3][0]
    if right == left + 1 or bottom == top + 1:
        return False
    for r, row in enumerate(sq):
        for c, count in enumerate(row):
            score = 3 if top < r < bottom else 1 if r in (top, bottom) else 0
            score += 3 if left < c < right else 1 if c in (left, right) else 0
            if count != (0, 0, 1, 0, 2, None, 4)[score]:
                return False
    return True

main()
