class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = Counter(ages)
        distinct_ages = set(age_count.keys())
        total_req = 0
        for a_age in distinct_ages:
            a_frn_req = 0
            for b_age in distinct_ages:
                if b_age > a_age or a_age < 100 < b_age or b_age <= 0.5 * a_age + 7:
                    continue
                a_frn_req += age_count[a_age] * age_count[b_age]
                if a_age == b_age:
                    a_frn_req -= age_count[a_age]
            total_req += a_frn_req
        return total_req
