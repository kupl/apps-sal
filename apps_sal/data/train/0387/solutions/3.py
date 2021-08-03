class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        N = len(votes[0])
        mapping = collections.defaultdict(lambda: [0 for _ in range(N)])
        for v in votes:
            for i, char in enumerate(v):
                mapping[char][i] += 1
        return ''.join([candidate for candidate, _ in sorted(mapping.items(), key=lambda x:(x[1], -ord(x[0])), reverse=True)])
