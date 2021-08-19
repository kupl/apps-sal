def get_opposite_vote(vote):
    return 'R' if vote == 'D' else 'D'


def codeforces(votes):
    blocked = {'R': 0, 'D': 0}
    while True:
        new_votes = ''
        for vote in votes:
            if blocked[vote] > 0:
                blocked[vote] -= 1
            else:
                blocked[get_opposite_vote(vote)] += 1
                new_votes += vote
        votes = new_votes
        if votes.count('R') == 0 or votes.count('D') == 0:
            break
    return votes[0]


_ = input()
votes = input()
print(codeforces(votes))
