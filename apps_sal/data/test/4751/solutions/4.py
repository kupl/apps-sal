class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        check = set()
        while cur:
            if cur in check:
                return True
            check.add(cur)
            cur = cur.next
        return False
