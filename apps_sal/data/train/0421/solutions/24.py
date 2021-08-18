class Solution:
    def lastSubstring(self, s: str) -> str:

        candidate_indices = list(range(len(s)))
        index_offset = 0

        while len(candidate_indices) > 1:
            current_max = max([s[candidate + index_offset] for candidate in candidate_indices if candidate + index_offset < len(s)])

            new_candidates = []

            for i, candidate in enumerate(candidate_indices):

                if i > 0 and candidate_indices[i - 1] + index_offset == candidate:
                    continue

                if candidate + index_offset > len(s) - 1:
                    break

                if s[candidate + index_offset] == current_max:
                    new_candidates.append(candidate)

            candidate_indices = new_candidates
            index_offset += 1

        return s[candidate_indices[0]:]
