class Solution:
    def lastSubstring(self, s: str) -> str:

        candidate_indices = list(range(len(s)))
        offset = 0

        while len(candidate_indices) > 1:
            current_max = max([s[candidate + offset] for candidate in candidate_indices if candidate + offset < len(s)])
            new_candidates = []

            for i, candidate in enumerate(candidate_indices):

                if i >= 1 and candidate_indices[i - 1] + offset == candidate:
                    # Swallow
                    continue

                if candidate + offset >= len(s):
                    break

                if s[candidate + offset] == current_max:
                    new_candidates.append(candidate)

            candidate_indices = new_candidates
            offset += 1

        return s[candidate_indices[0]:]
